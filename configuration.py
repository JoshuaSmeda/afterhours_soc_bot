SLA_SETTINGS = {
  'SEVERITY_1': {'ENABLED': True, 
  'LOW_SEVERITY': {'TIMER': 800, 'NOTIFICATION_METHOD': 'TEST'}, 
  'MEDIUM_SEVERITY': {'TIMER': 100, 'NOTIFICATION_METHOD': 'DOG'}}
}

SYSTEM_SETTINGS = {
    'SEVERITY_LEVEL': 3,
    'HIVE_SERVER_IP': '192.168.1.15',
    'HIVE_SERVER_PORT': 9000,
    'HIVE_FQDN': 'http://192.168.1.15',
    'HIVE_API_KEY': 'iIMm25V63IjkoLN0MlsJJTcdrPYYhyBi',
    'LOG_FILE_LOCATION': 'debug.log'
}

FLASK_SETTINGS = {
    'ENABLE_WEBSERVER': True,
    'FLASK_WEBSERVER_IP': '192.168.1.200',
    'FLASK_WEBSERVER_PORT': 3000
}

TWILIO_SETTINGS = {
    'TWILIO_ENABLED': True,
    'TWILIO_SENDER': '+123456789',
    'TWILIO_RTCP': ['+123456789', '+123456789'],
    'ACCOUNT_SID': '',
    'AUTH_TOKEN': '',
    'TWIMLET_URL': 'http://twimlets.com/echo?Twiml=%3CResponse%3E%3CSay%3EHi+there.%3C%2FSay%3E%3C%2FResponse%3E'
}

SLACK_SETTINGS = {
    'SLACK_ENABLED': True,
    'SLACK_APP_TOKEN': '',
    'SLACK_CHANNEL': '',
    'SLACK_WEBHOOK_URL': ''
}
