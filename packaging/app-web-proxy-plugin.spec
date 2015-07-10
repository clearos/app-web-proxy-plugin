
Name: app-web-proxy-plugin
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: Web Proxy Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-web-proxy-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Web Proxy Policies provide access control for the Web Proxy app.

%package core
Summary: Web Proxy Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Web Proxy Policies provide access control for the Web Proxy app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/web_proxy_plugin
cp -r * %{buildroot}/usr/clearos/apps/web_proxy_plugin/

install -D -m 0644 packaging/web_proxy.php %{buildroot}/var/clearos/accounts/plugins/web_proxy.php

%post core
logger -p local6.notice -t installer 'app-web-proxy-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/web_proxy_plugin/deploy/install ] && /usr/clearos/apps/web_proxy_plugin/deploy/install
fi

[ -x /usr/clearos/apps/web_proxy_plugin/deploy/upgrade ] && /usr/clearos/apps/web_proxy_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-web-proxy-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/web_proxy_plugin/deploy/uninstall ] && /usr/clearos/apps/web_proxy_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/web_proxy_plugin/packaging
%dir /usr/clearos/apps/web_proxy_plugin
/usr/clearos/apps/web_proxy_plugin/deploy
/usr/clearos/apps/web_proxy_plugin/language
/var/clearos/accounts/plugins/web_proxy.php
