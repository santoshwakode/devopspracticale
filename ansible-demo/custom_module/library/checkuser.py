from ansible.module_utils.basic import *

def is_user_exist(username):
  try:
    import pwd
    #return (username in [entry.pw_name for entry in pwd.getpwall()])
    return [user.pw_shell for user in pwd.getpwall() if username.pw_name == "root"][0]
  except:
    module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
    module.fail_json(msg="Module pwd not found")

def main():
  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  usershell = module.params.get("usershell")
  
  exists = is_user_exist(username)
  if exists:
    msg = "{0} is found".format(username)
  else:
    msg = "{0} is not found".format(username)

  module.exit_json(changed=True, msg=msg)
  

main()
