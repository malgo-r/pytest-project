import json
from unittest import TestCase

import pytest
from django.test import Client
from django.urls import reverse

from api.coronatech.companies.models import Company


companies_url = reverse("companies-list")
pytestmark = (
    pytest.mark.django_db
)  # this mark requests db access - creates new empty database for tests


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists_should_succeed(client) -> None:
    test_company = Company.objects.create(name="ESA")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_company.name
    assert response_content.get("status") == test_company.status
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_without_argument_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    response_content = json.loads(response.content)
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="ESA")
    response = client.post(
        path=companies_url,
        data={"name": "ESA"},
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "N7Space"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "N7Space"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_should_succeed(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "N7Space", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "N7Space", "status": "Test Status"}
    )
    assert response.status_code, 400
    assert "Test Status" in str(response.content)
    assert "is not a valid choice" in str(response.content)


@pytest.mark.xfail
def test_should_fails_which_is_ok() -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 2 == 2


# testing error rising
def raises_value_error_should_pass() -> None:
    if 2 > 1:
        raise AssertionError("2 should be bigger than 1")


def test_raises_value_error_should_pass() -> None:
    with pytest.raises(AssertionError) as e:
        raises_value_error_should_pass()

    assert str(e.value) == "2 should be bigger than 1"


# testing logging messages
import logging

logger = logging.getLogger("CoronaLogs")


def function_that_logs_something() -> None:
    try:
        raise ValueError("Some value error")
    except ValueError as e:
        logger.warning("Value error occured")


def test_warning_logging_should_pass(caplog) -> None:
    function_that_logs_something()
    assert "Value error occured" in caplog.text
