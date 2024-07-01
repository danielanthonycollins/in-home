filtering issue when trying to add icons to specific categories. Was missing the .name from the if statement so the conditions couldn't be met

Toasts bug where the jquery was causing the toast not to load as it didn't recognise the toast() function. Replaced it with vanilla javascript which worked with the bootstrap version I was using.

Emails issue after deploying, when setting up contact form getting SMTP.starttls() error and form not submitting correctly