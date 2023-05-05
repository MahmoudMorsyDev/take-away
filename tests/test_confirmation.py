from lib.confirmation import SendConfirmation
from unittest.mock import  Mock

    
def test_send_confirmation_with_Mock():
    mock_vonage = Mock()
    mock_sms = Mock()
    mock_vonage.sms = mock_sms 
    mock_sms.send_message.return_value ={
        "messages":[{'status':"0"}]
    }
    send_confirmation =SendConfirmation("4915158852831", mock_vonage)
    assert send_confirmation.send_confirmation_sms() == "Sent"
    mock_sms.send_message.assert_called_once_with({
        'from': 'Vonage APIs',
        'to': '4915158852831',
        'text': 'Thank you! Your order was placed and will be delivered before 18:52'
    })
