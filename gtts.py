"""
ADVANCED DISCERNMENT AUTOMATA (ADA)
Copyright (C) 2023 Tesseract Software & Technologies Inc.
All rights reserved.

Description:
This Python program is an AI application inspired by Jarvis, designed to provide voice-based responses to user inputs and perform various tasks on connected devices in a distributed manager environment. 
It incorporates features such as persistent short-term memory (STM) and long-term memory (LTM), introspection, and self-learning capabilities to adapt and utilize various tools effectively.

Key Features:

- Voice-based interaction:- The program utilizes voice input and output to engage in conversations with the user.
- Distributed Device Management:- It can manage and control connected devices within a distributed environment.
- Persistent STM and LTM:- The program employs short-term and long-term memory mechanisms to retain information and learn from past interactions.
- Introspection:- It has the ability to analyze its own processes, performance, and behavior for self-improvement.
- Self-Learning:- The AI program learns from its experiences and interactions to enhance its knowledge and utilization of different tools.
- Network Integration:- The AI program is designed to be part of a larger network of AI programs, where each program is monitored by a centralized super AI known as ADA.
- Encryption: We use RSA-256 encryption to encrypt and decrypt data stored on your devices, the encryption key is tied to your application license key.


Note: This program is a work in progress and subject to continuous improvements and updates.


Module Description:
This module contains all the functionality related to the short term memory (STM). 
The stm object should be initialized when the application starts up.
Our stm object is in turn made of various langchain memory objects, like  combined memory (zep memory + entity memory), conversationsummarybuffer
We used the Conversationsummarybuffer object to make various other type of memories like taskmanager memory, inference memory, introspection memory, and self-learning memory.
----tasksmanager memory, inference memory, introspection memory, and conmbined memory all have a READ ONLY version, that should be used every time this memories are supposed to be shared among diff processes as resource.
This module also contain methods to deal with zep memory server startup and initialization, also contains methods to get relevant messages that needs to be updated to the nexus.


Author: MD Jalal Uddin
Postion: Web Developer
Email: jalal.uiddin806090@gmail.com

Date: 2023-05-30
Version: 1.0.0

Dependencies:

langchain==0.0.173
    aiohttp==3.8.4
    aiosignal==1.3.1
    async-timeout==4.0.2
    attrs==23.1.0
    certifi==2023.5.7
    charset-normalizer==3.1.0
    dataclasses-json==0.5.7
    frozenlist==1.3.3
    greenlet==2.0.2
    idna==3.4
    marshmallow==3.19.0
    marshmallow-enum==1.5.1
    multidict==6.0.4
    mypy-extensions==1.0.0
    numexpr==2.8.4
    numpy==1.24.3
    openapi-schema-pydantic==1.2.4
    packaging==23.1
    pydantic==1.10.7
    PyYAML==6.0
    requests==2.30.0
    SQLAlchemy==2.0.13
    tenacity==8.2.2
    typing-inspect==0.8.0
    typing_extensions==4.5.0
    urllib3==2.0.2
    yarl==1.9.2

python-dotenv==1.0.0
openai==0.27.6
    tqdm==4.65.0

tiktoken==0.4.0
    regex==2023.5.5
    
anyio==3.6.2
h11==0.14.0
httpcore==0.17.1
nest_asyncio==1.5.6
zep-python==0.25



Usage:
suppose to be imported/Inherited from

Privacy:
This software respects your privacy. We are committed to protecting the privacy and security of your information.
This Privacy Policy outlines how we collect, use, and safeguard the data gathered through our AI application ("ADA"). 
By using the App, you consent to the practices described in this Privacy Policy. 
Any personal data that is collected will be handled in accordance with our privacy policy, which can be found at [URL to privacy policy].

DISCLAIMER:
The following disclaimer is intended to outline the limitations of responsibility and liability for the use of the AI program ("ADA"). By using the Program, you agree to the terms outlined in this disclaimer.

    +Program Intended Use:
    The Program is designed to provide specific functionalities and perform tasks as described in the provided documentation. It is intended for general-purpose use and does not endorse or support any illegal activities.

    +User Responsibility:
    As a user of the Program, you bear full responsibility for your actions and the consequences that may arise from using the Program. You must comply with all applicable laws, regulations, and ethical guidelines governing your jurisdiction. It is your sole responsibility to ensure that your actions align with legal and ethical standards.

    +Limitation of Liability:
    The creators and contributors of the Program shall not be held liable for any damages, losses, or legal consequences resulting from the use, misuse, or inability to use the Program. This includes, but is not limited to, damages arising from the creation of weapons, development or release of viruses, hacking attempts, or any other illegal activities conducted by individuals using the Program.

    +Third-Party Actions:
    The Program may interact with or provide access to third-party systems, applications, or services. The creators and contributors of the Program shall not be held responsible for any actions, damages, or consequences resulting from the use of such third-party systems, applications, or services. Users are solely responsible for their interactions and engagements with third-party entities.

    +Security and Compliance:
    While efforts are made to ensure the security and integrity of the Program, the creators and contributors do not guarantee the absence of vulnerabilities or risks associated with its use. Users are responsible for implementing appropriate security measures and compliance protocols to protect their own systems and data.

    +Modification and Distribution:
    You may not modify, alter, or redistribute the Program without explicit permission from the creators and contributors. Any unauthorized modifications or distribution are done at your own risk, and the creators and contributors shall not be liable for any consequences resulting from such unauthorized actions.

    +No Warranty:
    The Program is provided on an "as-is" basis, without warranties or conditions of any kind, either expressed or implied. The creators and contributors do not make any warranties or representations regarding the accuracy, reliability, or suitability of the Program for any particular purpose.

    +Legal Advice:
    This disclaimer does not constitute legal advice. Users are advised to consult with legal professionals to ensure compliance with applicable laws and regulations, especially concerning the specific use cases and functionalities of the Program.

By using the Program, you acknowledge that you have read and understood this disclaimer and agree to release the creators and contributors from any legal responsibility or liability arising from the use or misuse of the Program.
"""
from gtts import gTTS
import pygame
from io import BytesIO

############################################ ---GLOBAL VARIABLES---###############################################################################################
# Global variables in Python are variables that are declared outside of all function definitions and are accessible throughout the entire program, in all scopes. Unlike local variables, which only exist and can be accessed within the function they are defined in, global variables can be accessed from any function or method in your program.

# In Python, you define a global variable by assigning a value to a variable name outside any function or class. Here's a basic example:

# ```python
# global_variable = "This is a global variable."
# ```

# You can access the global variable from any function or method, like so:

# ```python
# def print_global():
#     print(global_variable)  # Output: This is a global variable.
# print_global()
# ```

# To modify a global variable from within a function, you need to declare it as global within that function, like this:

# ```python
# def modify_global():
#     global global_variable
#     global_variable = "The global variable has been modified."
# ```

# Global variables are typically used for constants or configuration settings that need to be accessed from multiple places within your program. However, overuse of global variables can make your code harder to understand and debug, so they should be used sparingly.

##################################################################################################################################################################

############################################ ---CLASS VARIABLES---###############################################################################################
# Class variables in Python are variables that are shared by all instances of a class. They belong to the class itself, rather than any single instance of the class. Unlike instance variables, which can have different values for each instance of a class, class variables have the same value for all instances.

# In Python, you define a class variable by assigning a value to a variable name inside the class but outside any method. Here's a basic example:

# 1. Import necessary libraries: gTTS from gtts, pygame, BytesIO from io.

# 2. Create a SpeechPlayer class:
#    1. Initialize the class with the given text, language, and tld.
#    2. Define a method named create_audio:
#       1. Create a gTTS object with the text, language, and tld.
#       2. Create a BytesIO object to store the audio data.
#       3. Write the audio data to the BytesIO object using gTTS write_to_fp method.
#       4. Move the position of the BytesIO object to the beginning.
#       5. Return the BytesIO object.
#    3. Define a method named play_audio:
#       1. Initialize the Pygame mixer.
#       2. Create the audio data by calling the create_audio method.
#       3. Load the audio data into the Pygame mixer.
#       4. Play the audio using pygame.mixer.music.play().
#       5. Enter a loop and wait until the audio finishes playing by checking pygame.mixer.music.get_busy().
#       6. Shut down the Pygame mixer.

# 3. Create an instan0ce of the SpeechPlayer class with the given text.

# 4. Call the play_audio method on the SpeechPlayer instance to play the audio.

# 5. End of the program.

# Class variables are typically used for data that should be shared across all instances of a class, such as configuration settings or fixed values that do not change from one instance to another.

##################################################################################################################################################################

# @global class variables


class SpeechPlayer:
    def __init__(self, text, language="en", tld="ca"):
        self.text = text
        self.language = language
        self.tld = tld

    def create_audio(self):
        # Create a gTTS object and generate audio from the given text
        tts = gTTS(self.text, lang=self.language, tld=self.tld)
        audio_data = BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    def play_audio(self):
        # Initialize the pygame mixer
        pygame.mixer.init()

        # Create the audio from the text
        audio_data = self.create_audio()

        # Load the audio into pygame mixer and play it
        pygame.mixer.music.load(audio_data)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Quit the pygame mixer
        pygame.mixer.quit()


# Create an instance of SpeechPlayer with the desired text
text = "ChatGPT is a natural language processing tool driven by AI technology that allows you to have human-like conversations and much more with the chatbot. The language model can answer questions and assist you with tasks, such as composing emails, essays, and code."
player = SpeechPlayer(text)

# Play the audio
player.play_audio()
