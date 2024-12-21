import openai
from config.settings import Settings
from services.logging_service import logging_service

class NLPService:
    def __init__(self):
        self.settings = Settings()
        openai.api_key = self.settings.OPENAI_API_KEY

    async def generate_response(self, prompt, max_tokens=100):
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.settings.NLP_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging_service.error(f"Error in NLP service: {str(e)}")
            return None

    async def summarize_text(self, text, max_tokens=50):
        prompt = f"Summarize the following text in {max_tokens} tokens or less:\n\n{text}"
        return await self.generate_response(prompt, max_tokens)

    async def generate_hashtags(self, text, num_hashtags=5):
        prompt = f"Generate {num_hashtags} relevant hashtags for the following text:\n\n{text}"
        response = await self.generate_response(prompt)
        if response:
            return [tag.strip() for tag in response.split() if tag.startswith('#')]
        return []

    async def detect_intent(self, text):
        prompt = f"Classify the intent of the following text into one of these categories: question, statement, command, or other:\n\n{text}"
        return await self.generate_response(prompt)

    async def generate_poll_options(self, topic, num_options=4):
        prompt = f"Generate {num_options} poll options for the topic: {topic}"
        response = await self.generate_response(prompt)
        if response:
            return [option.strip() for option in response.split('\n') if option.strip()]
        return []

