import os, notify2
from dotenv import load_dotenv

load_dotenv()

notify2.init('notifier')

def command(cmd):
  os.system(cmd)

def sendNotif(body):
  notify2.Notification("Auto Git Pull",body,"notification-message-im").show()

def fetchOrigin():
  command("git fetch origin")

def pullMaster():
  command("git checkout master && git pull origin master")

workdir = os.getenv('WORKDIR')

print(workdir)

repolist = ["capi",
            "chef-free",
            "course",
            "crm",
            "dns",
            "forum",
            "helm",
            "panel",
            "partner",
            "qa",
	          "terraform",
            "www"]

current_dir = ""

try:
  sendNotif(body=f"Pull master branch on {workdir}")

  for repo in repolist:
    dir = workdir + repo
    current_dir = dir
    os.chdir(dir)
    sendNotif(body=f"Pulling on {dir}")
    command(f"echo 'pulling on {dir}' >> /home/belly/project-python/auto-git-pull/pull.log")
    fetchOrigin()
    pullMaster()

  sendNotif(body="Pull master branch complete!")
except:
  sendNotif(body=f"Pull master branch Failed on {current_dir}")
