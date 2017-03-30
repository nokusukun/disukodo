import glob
import importlib.util
from os.path import basename
from base.Map import Map
from base import EmbedUtils as embed
import traceback


class ModuleLoader():
    modules = []

    def __init__(self):
        # Finds all of the python files
        modules = glob.glob("modules/*.py", recursive=True)

        # Taken from: http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
        for x in modules:
            print("ModLoader --> {0}".format(basename(x)[:-3]))
            spec = importlib.util.spec_from_file_location(basename(x)[:-3], x)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self.modules.append(mod.Module())


    async def execute(self, **options):
        options = Map(options)

        for mod in self.modules:
            commands = getattr(mod.loader, options.cmdtype)
            
            if options.command is None:
                for func in list(commands.values()):
                    try:
                        print("[cmd:{0}] ?> {1}".format(options.cmdtype, func.__name__))
                        await func(options.event, options.client)
                    except:
                        print(traceback.print_exc())
                return


            print("[cmd:{0}] ?> {1}".format(options.cmdtype, options.command))
            
            if options.command in commands:
                print("[cmd:{0}] OK> {1}".format(options.cmdtype, options.event.args))
                user_roles = [x.name for x in options.event.user.roles]
                print("user_roles: {0}".format(user_roles))



                try:
                    await commands[options.command](options.event, options.client)
                except:

                    try:
                        print("[cmd:{0}] !".format(options.cmdtype))
                        em = embed.err_invalid(mod.loader._help[options.command], options.client)
                        print(em)
                        await options.client.send_message(options.event.message.channel,
                                                    embed=em)
                    except:

                        print("[cmd:{0}] !!".format(options.cmdtype))
                        em=embed.err_invalid("Generic command Error!", options.client)
                        print(em)
                        await options.client.send_message(options.event.message.channel, 
                                                    embed=em)
