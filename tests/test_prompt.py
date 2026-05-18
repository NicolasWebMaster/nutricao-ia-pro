from app.prompts import SYSTEM_PROMPT


def test_prompt():

    assert "Não invente informações" in SYSTEM_PROMPT
