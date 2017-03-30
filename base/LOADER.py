from base.COMMANDS import cmdtype
from base import ROLES
import asyncio

class CommandLoader():
    _scope = {}
    _role = {}
    _help = {}
    _noerr = {}

    Command = {}

    Message = {}
    Typing = {}
    Delete = {}
    Edit = {}
    Mention = {}
    Ready = {}

    ReactAdd = {}
    ReactRemove = {}
    ReactClear = {}

    ChannelAdd = {}
    ChannelRemove = {}

    MemberJoin = {}
    MemberLeave = {}
    MemberUpdate = {}
    MemberBan = {}
    MemberUnban = {}

    BotJoin = {}

    ServerDisable = {}
    ServerEnable = {}
    ServerChange = {}

    RoleAdd = {}
    RoleRemove = {}
    EmojiUpdate = {}

    VoiceUpdate = {}

    def cmdhelp(self, name):
        def deco(f):
            self._help[name] = f()

        return deco

    def command(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                #setattr(self, coro.__name__, coro)
                self._role[name] = ROLES.EVERYONE
                if "role" in options:
                    self._role[name] = options["role"]

                if "no_error" in options:
                    self._noerr[name] = options["no_error"]
                self.Command[name] = f
                print('\tLOAD_OK: {0.__name__}: on_command @ {1}: {2}'.format(f, name, self._role[name]))

        return deco

    def message(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                #setattr(self, coro.__name__, coro)
                self._role[name] = ROLES.EVERYONE
                if "role" in options:
                    self._role[name] = options["role"]

                self.Message[name] = f
                print('\tLOAD_OK: {0.__name__}: on_message @ {1}: {2}'.format(f, name, self._role[name]))

        return deco

    def mention(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                #setattr(self, coro.__name__, coro)
                self._role[name] = ROLES.EVERYONE
                if "role" in options:
                    self._role[name] = options["role"]

                self.Mention[name] = f
                print('\tLOAD_OK: {0.__name__}: on_mention @ {1} with role {2}'.format(f, name, self._role[name]))

        return deco

    def typing(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.Typing[name] = f
                print('\tLOAD_OK: {0.__name__}: on_typing @ {1}'.format(f, name))

        return deco

    def delete(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                self.Delete[name] = f
                print('\tLOAD_OK: {0.__name__}: on_delete @ {1}.'.format(f, name))

        return deco

    def edit(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.Edit[name] = f
                print('\tLOAD_OK: {0.__name__}: on_edit @ {1}'.format(f, name))

        return deco

    def ready(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.Ready[name] = f
                print('\tLOAD_OK: {0.__name__}: on_ready @ {1}'.format(f, name))

        return deco

    def reactadd(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.ReactAdd[name] = f
                print('\tLOAD_OK: {0.__name__}: react_add @ {1}'.format(f, name))

        return deco

    def reactremove(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.ReactRemove[name] = f
                print('\tLOAD_OK: {0.__name__}: react_remove @ {1}'.format(f, name))

        return deco

    def reactclear(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.ReactClear[name] = f
                print('\tLOAD_OK: {0.__name__}: react_clear @ {1}'.format(f, name))

        return deco

    def channeladd(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.ChannelAdd[name] = f
                print('\tLOAD_OK: {0.__name__}: channel_add @ {1}'.format(f, name))

        return deco

    def channelremove(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.ChannelRemove[name] = f
                print('\tLOAD_OK: {0.__name__}: channel_remove @ {1}'.format(f, name))

        return deco

    def memberjoin(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:
                
                self.MemberJoin[name] = f
                print('\tLOAD_OK: {0.__name__}: member_join @ {1}'.format(f, name))

        return deco

    def memberleave(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.MemberLeave[name] = f
                print('\tLOAD_OK: {0.__name__}: member_leave @ {1}'.format(f, name))

        return deco

    def memberupdate(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.MemberUpdate[name] = f
                print('\tLOAD_OK: {0.__name__}: member_update @ {1}'.format(f, name))

        return deco

    def ban(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.MemberBan[name] = f
                print('\tLOAD_OK: {0.__name__}: member_ban @ {1}'.format(f, name))

        return deco

    def unban(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.MemberUnban[name] = f
                print('\tLOAD_OK: {0.__name__}: member_unban @ {1}'.format(f, name))

        return deco

    def botjoin(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.BotJoin[name] = f
                print('\tLOAD_OK: {0.__name__}: bot_join @ {1}'.format(f, name))

        return deco

    def serverenable(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.ServerEnable[name] = f
                print('\tLOAD_OK: {0.__name__}: server_enable @ {1}'.format(f, name))

        return deco

    def serverdisable(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.ServerDisable[name] = f
                print('\tLOAD_OK: {0.__name__}: server_disable @ {1}'.format(f, name))

        return deco

    def serverchange(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.ServerChange[name] = f
                print('\tLOAD_OK: {0.__name__}: server_change @ {1}'.format(f, name))

        return deco

    def roleadd(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.RoleAdd[name] = f
                print('\tLOAD_OK: {0.__name__}: roleadd @ {1}'.format(f, name))

        return deco

    def roleremove(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.RoleRemove[name] = f
                print('\tLOAD_OK: {0.__name__}: roleremove @ {1}'.format(f, name))

        return deco

    def emojichange(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.EmojiUpdate[name] = f
                print('\tLOAD_OK: {0.__name__}: emojichange @ {1}'.format(f, name))

        return deco

    def voicechange(self, name, **options):

        def deco(f):
            if not asyncio.iscoroutinefunction(f):
                print('{0.__name__} command must be a coroutine'.format(f))

            else:

                self.VoiceUpdate[name] = f
                print('\tLOAD_OK: {0.__name__}: voicechange @ {1}'.format(f, name))

        return deco