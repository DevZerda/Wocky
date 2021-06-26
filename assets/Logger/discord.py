import os, sys, time

from discord_webhook import DiscordWebhook

class Discord:
	def send_news(msg):
		msg = f"{msg}"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855875753999859772/l5HDRhwRNUBI69M5lOlVI93fIx8tS99yMOOXgkl9s0jxozHSbP0wxdeHY9q_rhcSHl89', content=msg)
			webhook.execute()
			print("sent")
		except:
			print("Failed to send discord notification!")
		return ""

	def send_status(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855875753999859772/l5HDRhwRNUBI69M5lOlVI93fIx8tS99yMOOXgkl9s0jxozHSbP0wxdeHY9q_rhcSHl89', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_attack(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855836697374883850/R5x5ABjxgZux4SdDcS899SxehEkIEaLIRKxO_HELlmVal8xYC2EPIvwMzifreLPd7Syd', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_login(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855836899982049290/IzVYEFuEMM0muEeXSM0lQcbK93Xw2xEffcqHUjILmhGKbj7nhnr4XcZlB_2v-22zN4lI', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_logs(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855628566557753344/9ykjtzdWUFP0RsAoARs9m3R2nJZSPoPJ2KR9wLdmzIpUdazXqUeaMOfVUE3F3MNCeFkS', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")