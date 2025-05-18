# discord-scheduled-message-sender

## Opis (Polski)
Ten skrypt w Pythonie umożliwia automatyczne wysyłanie wiadomości na Discordzie w określonych odstępach czasu. Dodatkowo, istnieje możliwość automatycznego usuwania wysłanych wiadomości po ich wysłaniu np, do boostowania postów na forum. (działa na kanałach tekstowych oraz postach forum)

### Konfiguracja
Plik `config.json` zawiera ustawienia wymagane do działania skryptu:
- `token`: Twój token bota Discord.
- `messages`: Lista wiadomości do wysłania. Każdy element listy zawiera:
  - `channel_id`: ID kanału, na który wiadomość ma zostać wysłana.
  - `message`: Treść wiadomości.
  - `interval`: Odstęp czasu w formacie `10s`, `10m`, `10h`, `10d`.
  - `delete`: (opcjonalne) Czy wiadomość ma zostać usunięta po wysłaniu (wartość `true` lub `false`).

Przykład pliku `config.json`:
```json
{
  "token": "YOUR_TOKEN",
  "messages": [
    {
      "channel_id": 1234567890123456789,
      "message": "Przykładowa wiadomość",
      "interval": "10s",
      "delete": true
    }
  ]
}
```

---

## Description (English)
This Python script allows you to automatically send messages on Discord at specified intervals. Additionally, it can automatically delete sent messages after they are sent eg. for boosting posts on forum. (working on text and forum post channels)

### Configuration
The `config.json` file contains the settings required for the script to work:
- `token`: Your Discord bot token.
- `messages`: A list of messages to send. Each list item includes:
  - `channel_id`: The ID of the channel where the message will be sent.
  - `message`: The content of the message.
  - `interval`: Time interval in the format `10s`, `10m`, `10h`, `10d`.
  - `delete`: (optional) Whether the message should be deleted after being sent (`true` or `false`).

Example `config.json` file:
```json
{
  "token": "YOUR_TOKEN",
  "messages": [
    {
      "channel_id": 1234567890123456789,
      "message": "Example message",
      "interval": "10s",
      "delete": true
    }
  ]
}

