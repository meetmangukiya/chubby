# github3.py License
# ==================
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import github3
import getpass
import datetime
import logging

import chubby.config as config

logger = logging.getLogger(__name__)

def create_token(username: str):
    """
    Create token for a given username.

    :param username:
        Username of the account whose token has to be created.
    :returns:
        github3 Authorization object.
    """
    password = getpass.getpass()
    def two_factor_auth():
        logger.info('Needs 2FA')
        token = ''
        logger.debug('Taking 2FA code from user...')
        while not token:
            token = input("Enter 2FA code: ")
        return token

    return github3.authorize(login=username,
                             password=password,
                             scopes = ['user', 'repo'],
                             note="chubby: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()),
                             note_url="https://github.com/meetmangukiya/chubby",
                             two_factor_callback=two_factor_auth)

def save_to_config(username: str):
    """
    Create token for a given user and save it to the config file.
    :param username:
        Username for which token has to be created and saved to config.
    :returns:
        github3 login object.
    """
    if username in config.read_config().sections():
        logger.info('User already configured...')
        prompt = input("User already configured, do you want to force configure?[y/N]")
        prompt = 'N' if prompt != 'y' else 'y'
        if prompt == 'N':
            logger.info('Returning existing config...')
            return github3.login(token=config.read_config()[username]['token'])
        else:
            logger.info('Force overwriting existing config with new config...')
    auth = create_token(username)
    contents = {
        "token": auth.token,
        "id": auth.id,
        "username": username
    }
    config.write_config(username, contents)
    gh = github3.login(token=auth.token)
    return gh

def get_login(username: str):
    """
    Checks for token in the config file, if not create one.
    :returns:
        github3 login object
    """
    if not username:
        logger.warning("Config for {} doesn't exist, creating new section...")
        return save_to_config(username)
    return github3.login(token=config.read_config()[username]['token'])
