%global realname iterpipes

Name:           python-%{realname}
Version:        0.4
Release:        4%{?dist}
Summary:        Shell pipelines in Python using shell-like syntax
Group:          Development/Languages

License:        MIT
URL:            http://iterpipes.pirx.ru/
Source0:        https://pypi.python.org/packages/source/i/iterpipes/%{realname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description

Python is a good choice for many software tools, but it lacks clarity
and simplicity of command shells when it comes to running command
pipelines from scripts. The standard subprocess module provides basic
inter-processing tools, but it requires lots of lines to express a
single shell line.

iterpipes is trying to overcome this limitation by representing a
shell command pipeline as a function over iterables, similar to
functions from the standard itertools module.

%prep
%setup -q -n %{realname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%check
export PYTHONPATH=$(pwd)/build/lib
%{__python} test/test_iterpipes.py


%files
%doc LICENSE README TODO
%{python_sitelib}/*


%changelog
* Mon Apr  1 2013 John Morris <john@zultron.com> - 0.4-4
- initial package

