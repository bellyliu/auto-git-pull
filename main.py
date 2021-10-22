import os

def command(cmd):
  os.system(cmd)

def sendNotif(tittle,cmd=''):
  command(f"notify-send '{tittle}' {cmd}")

def fetchOrigin():
  command("git fetch origin")

def pullMaster():
  command("git checkout master && git pull origin master")

workdir = "/home/belly/work/"

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
            "www"]

current_dir = ""

try:
  sendNotif(f"Pull master branch on {workdir}")

  for repo in repolist:
    dir = workdir + repo
    current_dir = dir
    os.chdir(dir)
    sendNotif("Pulling on " + dir)
    command(f"echo 'pulling on {dir}' >> /home/belly/project-python/auto-git-pull/pull.log")
    fetchOrigin()
    pullMaster()

  sendNotif(f"Pull master branch complete!")
except:
  sendNotif(f"Pull master branch Failed on {current_dir}")