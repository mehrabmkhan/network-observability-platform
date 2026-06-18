from scripts.validate_configs import validate


def test_validate_configs_passes():
    assert validate() == []
