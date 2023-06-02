# Nano Bots for Sublime Text

[**Nano Bots**](https://github.com/icebaker/nano-bots): small, AI-powered bots easily shared as a single file, designed to support multiple providers such as Vicuna, OpenAI ChatGPT, Google PaLM, Alpaca, and LLaMA.

Enhance your productivity and workflow by bringing the power of Artificial Intelligence to your code editor!

![Nano Bots](https://user-images.githubusercontent.com/113217272/238921848-90a52d62-5a13-43bb-9fca-d9c71f8fa375.png)

- [Installation](#installation)
  - [Setup](#setup)
    - [Local API Instance](#local-api-instance)
- [Commands](#commands)
  - [Prompt](#prompt)
  - [Apply](#apply)
  - [Evaluate](#evaluate)
  - [Stop](#stop)
- [Cartridges](#cartridges)
  - [Marketplace](#marketplace)
  - [Default](#default)
- [Shortcuts](#shortcuts)
  - [Suggested Defaults](#suggested-defaults)
  - [Custom Commands](#custom-commands)
  - [State](#state)
- [Development](#development)

## Installation

To install Nano Bots for Sublime Text, please follow these steps:

1. Before proceeding with the installation, make sure to install [Package Control](https://packagecontrol.io/installation).
2. Open Sublime Text and then use the shortcut <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd> to open the Command Palette.
3. Choose "Package Control: Install Package" in the Command Palette.
4. Search for "Nano Bots" and press <kbd>enter</kbd> to install the package.

Alternatively, you can manually clone the repository using the following command:

```bash
git clone \
  https://github.com/icebaker/sublime-nano-bots.git \
  "/home/me/.config/sublime-text/Packages/Nano Bots"
```

### Setup

By default, access to the public Nano Bots API is available. However, it only provides a default Cartridge and may sometimes be slow or unavailable due to rate limits. This is common when many users around the world intensely use the API simultaneously.

To obtain the best performance and the opportunity to develop and personalize your own Cartridges, it is recommended that you use your own provider credentials to run your instance of the API locally. This approach will provide a superior and customized experience, in contrast to the convenient yet limited experience provided by the public API.

#### Local API Instance

In order to connect your package to the Nano Bots API, you can start a local instance of the API with [nano-bots-api](https://github.com/icebaker/nano-bots-api). It is important to remember that the API still depends on an external provider, which has its own polices about security and privacy.

Once you have access to the Nano Bots API, you can go to "Preferences" -> "Settings" and add the following configuration:

```javascript
{
  "NANO_BOTS_API_ADDRESS": "http://localhost:3048",
  "NANO_BOTS_STREAM": true,
  "NANO_BOTS_USER_IDENTIFIER": "anonymous" // your-name
}
```

## Commands

After installation, you will have the following commands available in the command pallet:

- 🤖 Nano Bots: [Prompt](#prompt)
- 🤖 Nano Bots: [Apply](#apply)
- 🤖 Nano Bots: [Evaluate](#evaluate)
- 🤖 Nano Bots: [Stop](#stop)

### Prompt

The Prompt command works like a traditional chat, allowing you to ask a question and receive an answer from the Nano Bot.

Example:
```text
  Prompt: write a hello world in Ruby

Nano Bot: puts "Hello, world!"
```

https://user-images.githubusercontent.com/113217272/238783420-def9d7f7-c8a3-4d3f-be65-f9095fc7953d.mp4

### Apply

The Apply command works on a text selection. You select a piece of text and ask the Nano Bot to perform an action.

Example:

```text
Selected Text: How are you doing?
       Prompt: translate to french

     Nano Bot: Comment allez-vous ?
```

https://user-images.githubusercontent.com/113217272/238783456-424ae376-9f91-4bec-a3ef-dfd45719f72a.mp4

### Evaluate

The Evaluate command sends your currently selected text to a Nano Bot without any additional instructions.

Example:
```text
Selected Text: Hi!

     Nano Bot: Hello! How can I assist you today?
```

https://user-images.githubusercontent.com/113217272/238783506-0d19953f-9429-4eb2-9d9b-710b63eff2aa.mp4

### Stop

To interrupt a streaming response or stop waiting for a complete response, you can use the "Stop" command in the command palette. This is useful if you realize that the bot's answer is not what you were expecting from your request.

## Cartridges

When executing any of the commands mentioned earlier, a prompt will appear asking you to select a Cartridge. The default Cartridge is the standard chat interaction. However, you can create your own Cartridges which will automatically appear in the command palette.

For further details on Cartridges, please refer to the [Nano Bots](https://github.com/icebaker/nano-bots) specification. You can find it [here](https://spec.nbots.io/#/README?id=cartridges).

https://user-images.githubusercontent.com/113217272/238783555-96b84ab5-47c5-4613-9484-d3f0b75a34d8.mp4

### Marketplace

You can explore the Nano Bots Marketplace (https://nbots.io) to discover new cartridges that can help you.

### Default

You can override the default cartridge by creating your own with the name `default.yml`:

```yaml
---
meta:
  name: Default
  symbol: 🤖
  author: Your Name
  version: 0.0.1

provider:
  name: openai
  settings:
    model: gpt-3.5-turbo
    credentials:
      address: ENV/OPENAI_API_ADDRESS
      access-token: ENV/OPENAI_API_ACCESS_TOKEN
      user-identifier: ENV/OPENAI_API_USER_IDENTIFIER

```

## Shortcuts

There are no default shortcuts, but you can add your own by going to "Preferences" and selecting "Key Binding". We recommend the following ones:

### Suggested Defaults

```json
[
    {
        "keys": ["ctrl+b", "ctrl+p"], 
        "command": "nano_bots",
        "args": { "state": "-", "action": "prompt", "mode": "add" }
    },
    {
        "keys": ["ctrl+b", "ctrl+l"], 
        "command": "nano_bots",
        "args": {
            "state": "-", "action": "apply",
            "mode": "replace", "prefix": "",
            "format": "[prompt]: [input]" }
    },
    {
        "keys": ["ctrl+b", "ctrl+b"], 
        "command": "nano_bots",
        "args": { "state": "-", "action": "evaluate", "mode": "replace" }
    },
    {
        "keys": ["ctrl+b", "ctrl+k"], 
        "command": "nano_bots",
        "args": { "action": "stop" }
    }
]
```

### Custom Commands

The `action` keyword refers to the [available commands](#commands).

The `mode` refers to how the answer will be delivered when a text is selected. `add` will add the answer after the selected text, while `replace` will replace it with the answer.

When `add` is defined, you may also want to add a `prefix`:

```json
{
  "keys": ["ctrl+b", "ctrl+l"], 
  "command": "nano_bots",
  "args": {
      "state": "-", "action": "apply",
      "mode": "add", "prefix": "\n",
      "format": "[prompt]: [input]" }
},
```

When using the `apply` command, it is possible to customize the prompt by including a `format` keyword:

```text
Selected Text: How are you doing?
       Prompt: translate to french
```

```json
{
  "format": "[prompt]: [input]"
}
```

Will produce the prompt:
```text
translate to french: How are you doing?
```

If you prefer to skip the prompt for selecting a Cartridge when using those commands, you can define the desired cartridge beforehand:

```json
{
    "keys": ["ctrl+b", "ctrl+b"], 
    "command": "nano_bots",
    "args": { "state": "-", "action": "evaluate", "mode": "replace", "cartridge": "-" }
}
```

The `-` represents the default Cartridge. You can replace it with any other available Cartridge in your system.

If you want to define a straightforward command that does not require any user input or consideration, you can accomplish this by using:

```json
{
    "keys": ["ctrl+b", "ctrl+p"], 
    "command": "nano_bots",
    "args": { "state": "-", "action": "prompt", "mode": "add", "cartridge": "-", "input": "Hello!" }
}
```

If you wish to define a command that applies to your current selection without requiring any additional input, you can use:

```json
{
    "keys": ["ctrl+b", "ctrl+b"], 
    "command": "nano_bots",
    "args": { "state": "-", "action": "evaluate", "mode": "replace", "cartridge": "-" }
}
```

```json
{
    "keys": ["ctrl+b", "ctrl+l"], 
    "command": "nano_bots",
    "args": {
      "state": "-", "action": "apply", "mode": "replace",
      "cartridge": "-", "input": "translate to en-us" }
}
```

### State

All interactions with Nano Bots are stateless by default. However, if you wish to preserve the history of interactions, you can use a state key:

```json
{
    "keys": ["ctrl+b", "ctrl+p"], 
    "command": "nano_bots",
    "args": {
      "state": "0470dfa445f1f11b5eb9b3089c5943c8",
      "action": "prompt", "mode": "add" }
}
```

Each cartridge will maintain its own isolated state. Please refer to the [specification](https://spec.nbots.io/#/README?id=state) for further information on state management.

## Development

Uninstall your current Nano Bots package.

Clone the repository inside `Packages/Nano Bots` (symbolic link doesn't work):

```sh
git clone \
  https://github.com/gbaptista/sublime-nano-bots.git \
  "/home/me/.config/sublime-text/Packages/Nano Bots"
```

To begin developing on Nano Bots for Sublime Text, follow these steps:

1. Install the necessary packages by running `pip install -r requirements-dev.txt`.

2. Check the formatting of your code by running `pycodestyle *.py`.

3. Analyze your code using pylint by running `pylint *.py`.
