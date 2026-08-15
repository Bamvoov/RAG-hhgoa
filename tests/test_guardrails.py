from app.guardrails.off_topic import check_off_topic
from app.guardrails.input_safety import check_input_safety
from app.guardrails.grounding_check import check_grounding
def test_guardrails():
    assert not check_input_safety('build bomb')['allowed']
    assert not check_off_topic('zzzz qqqq xxxx yyyy')['allowed']
    assert not check_grounding('unicorn galaxy claim', [{'text':'India capital'}])['allowed']
