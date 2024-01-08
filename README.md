# Nano Bots for Sublime Text

[Nano Bots](https://spec.nbots.io): AI-powered bots that can be easily shared as a single file, designed to support multiple providers such as [Cohere Command](https://cohere.com), [Google Gemini](https://deepmind.google/technologies/gemini), [Maritaca AI MariTalk](https://www.maritaca.ai), [Mistral AI](https://mistral.ai), [Ollama](https://ollama.ai), [OpenAI ChatGPT](https://openai.com/chatgpt), and others, with support for calling tools (functions).

Enhance your productivity and workflow by bringing the power of Artificial Intelligence to your code editor!

![Nano Bots](https://raw.githubusercontent.com/icebaker/assets/main/sublime-nano-bots/cover.png)

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
- [Privacy and Security: Frequently Asked Questions](#privacy-and-security-frequently-asked-questions)
  - [Will my files/code/content be shared or uploaded to third-party services?](#will-my-filescodecontent-be-shared-or-uploaded-to-third-party-services)
  - [What information may be shared with third-party AI providers?](#what-information-may-be-shared-with-third-party-ai-providers)
  - [Who are these third parties?](#who-are-these-third-parties)
  - [Is there an option to avoid sharing any information?](#is-there-an-option-to-avoid-sharing-any-information)
  - [Can I use this for private or confidential content/code?](#can-i-use-this-for-private-or-confidential-contentcode)
  - [Do I need to pay to use this?](#do-i-need-to-pay-to-use-this)
  - [Is this project affiliated with OpenAI?](#is-this-project-affiliated-with-openai)
  - [Warranty and Disclaimer](#warranty-and-disclaimer)
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

To connect your package to your own local Nano Bots API, start a local instance using [nano-bots-api](https://github.com/icebaker/nano-bots-api). Please note that the local API still relies on external providers, which has its own policies regarding security and privacy. However, if you choose to use [Ollama](https://ollama.ai) with open source Models, you can ensure that everything is kept local and remains completely private.

Once you have access to the Nano Bots API, you can go to "Preferences" -> "Settings" and add the following configuration:

```javascript
{
  "NANO_BOTS_API_ADDRESS": "http://localhost:3048",
  "NANO_BOTS_STREAM": true,
  "NANO_BOTS_END_USER": "anonymous" // your-name
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

You can explore the Nano Bots [Marketplace](https://nbots.io) to discover new cartridges that can help you.

### Default

You can override the default cartridge by creating your own with the name `default.yml`:

```yaml
---
meta:
  symbol: 🤖
  name: Default
  author: Your Name
  version: 1.0.0
  license: CC0-1.0
  description: A helpful assistant.

provider:
  id: openai
  credentials:
    address: ENV/OPENAI_API_ADDRESS
    access-token: ENV/OPENAI_API_KEY
  settings:
    user: ENV/NANO_BOTS_END_USER
    model: gpt-3.5-turbo
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

## Privacy and Security: Frequently Asked Questions

### Will my files/code/content be shared or uploaded to third-party services?

Absolutely not, unless you intentionally take action to do so. The files you're working on or have open in your editor will never be uploaded or shared without your explicit action.

### What information may be shared with third-party AI providers?

Only small fragments of text/code that you intentionally take action to share. The text you input while using the [Prompt](#prompt) command is shared with the [Nano Bots Public API](https://api.nbots.io), which also needs to share it with the [OpenAI API](https://platform.openai.com/docs/api-reference) strictly for generating a response. If you use [Evaluate](#evaluate) or [Apply](#apply), the specific text you select will also be shared to produce a response.

### Who are these third parties?

The data you deliberately choose to share will be transmitted securely (HTTPS) to the [Nano Bots Public API](https://api.nbots.io). This public API is open source and available for auditing [here](https://github.com/icebaker/nano-bots-api). It employs [OpenAI API](https://platform.openai.com/docs/api-reference) for data processing. As a result, any data you opt to share will also be sent to OpenAI API, which according to [their policies](https://openai.com/policies/api-data-usage-policies), is not used for model training and is not retained beyond a 30-day period.

### Is there an option to avoid sharing any information?

Sharing fragments of data is necessary to generate outputs. You have the option to use your own [local instance](#local-api-instance) of the [Nano Bots API](https://github.com/icebaker/nano-bots-api). This setup ensures all interactions occur locally on your machine, with the only data shared being with your personal [OpenAI API](https://platform.openai.com). Alternatively, you can decide not to use OpenAI as well, and instead, connect the local Nano Bots API to your own local LLM, such as [FastChat](https://github.com/lm-sys/FastChat), enabling a completely local and private interaction.

### Can I use this for private or confidential content/code?

For private or confidential content/code, we recommend that you or your organization conduct a thorough security and privacy assessment. Based on this, you may decide that the [Nano Bots Public API](https://github.com/icebaker/nano-bots-api) and [OpenAI's privacy policies](https://openai.com/policies/api-data-usage-policies) are sufficient, or you may choose to use your own [private setup](#local-api-instance) for the API and LLM provider.

### Do I need to pay to use this?

No. If you're using the default [Nano Bots Public API](https://api.nbots.io), there's no cost involved, but you might encounter occasional rate limiting or stability issues. If you decide to use your own API and LLM provider, any associated costs will depend on your chosen provider. For instance, using the Nano Bots API locally with OpenAI will require a paid [OpenAI Platform Account](https://platform.openai.com).

### Is this project affiliated with OpenAI?

No, this is an open-source project with no formal affiliations with OpenAI. It's designed for compatibility with various LLM providers, with OpenAI being the default one. As OpenAI is a private company, we can't provide any assurances about their services, and we have no affiliations whatsoever. Use at your own risk.

### Warranty and Disclaimer

This project follows the [MIT license](https://opensource.org/license/mit/). In plain language, it means:

> The software is provided as it is. This means there's no guarantee or warranty for it. This includes how well it works (if it works as you expect), if it's fit for your purpose, and that it won't harm anything (non-infringement). The people who made or own this software can't be held responsible if something goes wrong because of the software, whether you're using it, changing it, or anything else you're doing with it.

In other words, there's no promise or responsibility from us about what happens when you use it. So, it's important that you use it at your own risk and decide how much you trust it. You are the one in charge and responsible for how you use it and the possible consequences of its usage.

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
