# for use like:
# ExclusiveArch:  %{go_arches}
# noarch builds(BuildArch: noarch) falls through,
# ending with no B(R)s and no test/build invocations
# Former "%go_arches"
# can't be empty...
%golang_arches   empty
%gccgo_arches    %{power64} s390x aarch64 %{ix86} x86_64 %{arm}
%go_arches       %golang_arches %gccgo_arches

# Where to set GOPATH for builds. Like:
# export GOPATH=$(pwd)/_build:%{gopath}
%gopath          %{_datadir}/gocode


# Override to specify version for buildrequiresgo and requiresgo
%global %gccgo_version %{nil}
%global %golang_version %{nil}

# To provide easy way to set Go B(R)s, with possible version override
%buildrequiresgo \
  %ifarch %golang_arches \
BuildRequires: golang %{?golang_version} \
  %else \
  %ifarch %gccgo_arches \
BuildRequires: gcc-go %{?gccgo_version} \
  %endif \
  %endif

%requiresgo \
  %ifarch %golang_arches \
Requires: golang %{?golang_version} \
  %else \
  %ifarch %gccgo_arches \
Requires: libgo %{?gccgo_version} \
  %endif \
  %endif

# gocommands -p option for setting additional GOPATH(s), all arguments are appended to the go command 
# Usage: gobuild -p /home/usr/go -v -race .(same for gotest)
# TODO: investigate possibile ways to override GOTOOLDIR as it is not possible to directly override it in current go commands
# so it is not possible to use go from gcc-go to build with golang(and probably in reverse)
# for golang:
# export GOROOT="/usr/lib/golang" \
# export GOTOOLDIR="/usr/lib/golang/pkg/tool/linux_amd64" \
# for gcc:    
# export GOROOT="/usr"\
# export GOTOOLDIR="/usr/libexec/gcc/x86_64-redhat-linux/5.0.1"\

%gobuild(p:) \
  %ifarch %golang_arches \
    GOPATH=%{-p*} go build -compiler gc %{*} \
  %else \
  %ifarch %gccgo_arches \
    GOPATH=%{-p*} go build -compiler gccgo -gccgoflags "$RPM_OPT_FLAGS" %{*} \
  %endif \
  %endif

%gotest(p:) \
  %ifarch %golang_arches \
    GOPATH=%{buildroot}/%{gopath}:%{gopath}:%{-p*} go test -compiler gc %{*} \
  %else \
  %ifarch %gccgo_arches \
    GOPATH=%{buildroot}/%{gopath}:%{gopath}:%{-p*} go test -compiler gccgo -gccgoflags "$RPM_OPT_FLAGS" %{*} \
  %endif \
  %endif
