def send_email(message, recipient, sender="university.help@gmail.com"):

    if recipient.endswith((".com", ".ru", ".net")) and sender.endswith((".com", ".ru", ".net")) and "@" in (recipient and sender):
        if recipient == sender:
            print("Невозможно отправить письмо самому себе.")
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ АДРЕС! Письмо отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email("Будь здоров.", "metas@gmail.com")
