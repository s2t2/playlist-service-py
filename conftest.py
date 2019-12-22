import os
import pytest

from app.pandora_service import PandoraService

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid configuring credentials on, and issuing requests from, the CI server"

#@pytest.fixture(scope="module") # module-level causes the authentication to persist and cause false positives in some tests. use it however, if you decide to login during initialization
@pytest.fixture()
def pandora_service():
    return PandoraService()
