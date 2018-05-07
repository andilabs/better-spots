import re

from time import sleep

import random
import string

from django.core.signing import SignatureExpired
from django.test import TestCase
from django.test.utils import override_settings

from accounts.factories import UserFactory
from utils.mailtrap import MailTrapAPIClient
from utils.signer import decrypt_data


@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class TestEmailVerification(TestCase):
    """
        We use mailtrap.io service for testing emails with REST API, so we validate that the email was really sent

    """

    @staticmethod
    def extract_url_from_email(message_string):
        return re.search("(?P<url>https?://[^\s]+)", message_string).group("url")

    @staticmethod
    def get_token(url):
        return url.split('/')[-2]

    def setUp(self):
        self.mailtrap_client = MailTrapAPIClient()
        self.email_address = '{}@example.com'.format(
            ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10))
        )
        _ = UserFactory(email=self.email_address)
        mailbox = self.mailtrap_client.get_mailboxes()[0]
        self.mailbox_id = mailbox['id']
        self.mails = self.mailtrap_client.get_messages_of_inbox(mailbox['id'])

    def test_email_with_token_was_sent_after_user_created(self):
        self.assertEqual(len([i for i in self.mails if i['to_email'] == self.email_address]), 1)

    def test_sent_verification_token_is_decrypted_correctly(self):
        this_email = [i for i in self.mails if i['to_email'] == self.email_address][0]
        url_token = self.extract_url_from_email(this_email['text_body'])
        token = self.get_token(url_token)
        decryption_result = decrypt_data(token)
        self.assertEqual(decryption_result['result'], self.email_address)

    def test_sent_verification_token_expires(self):
        this_email = [i for i in self.mails if i['to_email'] == self.email_address][0]
        url_token = self.extract_url_from_email(this_email['text_body'])
        token = self.get_token(url_token)
        sleep(3)
        with self.assertRaises(SignatureExpired):
            _ = decrypt_data(token, max_age=2)

    def tearDown(self):
        self.mailtrap_client.clear_inbox(self.mailbox_id)
