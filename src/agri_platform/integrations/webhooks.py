class WebhookDispatcher:
    def send(self, url, payload):
        return {"url": url, "status": "queued"}
