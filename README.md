# JZGoogleTranslatorForIOS
Quickly generate localizable.Strings for 20 different languages using Google Translate API

### Usage:
python3 runMe.py

###Input:
Localizable.strings (English)

### Output:
    - es.lproj/Localizable.strings
    - fr.lproj/Localizable.strings
    - it.lproj/Localizable.strings
    - ...

### Quick Start:
    1. [Enable the Google Translate API](https://cloud.google.com/translate/v2/getting_started) with billing (don't worry its cheap)
    2. [Create an API key](https://cloud.google.com/translate/v2/getting_started) for the Google Translate API.
    3. Copy your key into runMe.py
    4. Copy your Localizable.strings into the root of the project
    5. Run python3 runMe.py
    6. Copy the output into your iOS project

### To add another language:
    Add country codes to Google_IOS_Country_Codes.txt

### Supported Languages out of the box:
    - French
    - German
    - ChineseSimplified
    - ChineseTraditional
    - Japanese
    - Spanish
    - Spanish-Mexican
    - Italian
    - Dutch
    - Korean
    - Portuguese
    - Portuguese(Portugal)
    - Danish
    - Finnish
    - Norwegian-BokMal
    - Swedish
    - Russian
    - Polish
    - Turkish
    - Arabic
    - Thai
    - Czech
    - Hungarian
    - Catalan
    - Croatian
    - Greek
    - Hebrew
    - Romanian
    - Slovak
    - Ukrainian
    - Indonesian
    - Malay
    - Vietnamese
