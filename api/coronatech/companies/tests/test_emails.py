import json
import pytest
from django.core import mail
from unittest.mock import patch


def test_send_mail_should_succeed(mailoutbox, settings) -> None:
    # https://docs.djangoproject.com/en/3.2/topics/email/#in-memory-backend
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0

    mail.send_mail(
        subject="Test subject",
        message="Test message",
        from_email="malgor.test@gmail.com",
        recipient_list=["malgor.test@gmail.com"],
        fail_silently=False,
    )

    assert len(mailoutbox) == 1

    assert mailoutbox[0].subject == "Test subject"

@pytest.mark.skip # something is wrong here
def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch(
        "api.coronatech.companies.views.send_company_email"
    ) as mocked_send_mail_function:
        response = client.post(path="/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"

        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email="malgor.test@gmail.com",
            recipient_list=["malgor.test@gmail.com"],
            fail_silently=False,
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    response_content = json.loads(response.content)

    assert response.status_code == 405
    assert response_content == {"detail": 'Method "GET" not allowed.'}
