import pytest

@pytest.mark.parametrize("name", [
    ("python-pymongo"),
    ("puppet-mongodb"),
    ("mongodb-server"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("mongodb","27017"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://" + port)
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("mongod", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("conf_file", [
    ("mongod.conf"),
])
def test_main_services_files(File, conf_file):
    _file = File("/etc/" + conf_file)
    assert _file.exists
