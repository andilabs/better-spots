import os
import requests


class MailTrapAPIClient(object):
    domain = "https://mailtrap.io"

    @staticmethod
    def headers():
        return {'Api-Token': os.environ['MAILTRAP_TOKEN']}

    def _get(self, url, params=None):
        full_url = "{}{}".format(self.domain, url)
        return requests.get(full_url, params, headers=self.headers())

    def _patch(self, url, params=None):
        full_url = "{}{}".format(self.domain, url)
        return requests.patch(full_url, params, headers=self.headers())

    def get_mailboxes(self):
        """
        https://mailtrap.docs.apiary.io/#reference/inbox
        :return: list of mailboxes (only one element in free plan of mailtrap)
        """
        url = "/api/v1/inboxes"
        return self._get(url).json()

    def get_messages_of_inbox(self, inbox_id):
        """
        https://mailtrap.docs.apiary.io/#reference/message
        :param inbox_id: id of mailbox
        :return: list of messages inside mailbox
        """
        url = "/api/v1/inboxes/{inbox_id}/messages".format(inbox_id=inbox_id)
        return self._get(url).json()

    def clear_inbox(self, inbox_id):
        url = "/api/v1/inboxes/{inbox_id}/clean".format(inbox_id=inbox_id)
        return self._patch(url).json()
