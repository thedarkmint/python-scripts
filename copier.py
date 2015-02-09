#!/usr/bin/env python


import os
import socket
import commands
import nmap
import subprocess



admin_ip="192.168.4.59"
uid=os.getuid()
gid=os.getgid()
host_list =[]


def portscan():
  nm=nmap.PortScanner()
  d=nm.scan('192.168.4.1/24' ,'22')
#  scan_output=nm['192.168.4.59']['tcp'][22]['state']
  for host in nm.all_hosts():
    #print host
    ip=str(host)
    if nm[ip].has_tcp(22):
      scan=str(nm[ip]['tcp'][22]['state'])
      if scan=="open":
        host_list.append(ip)
        copy_scp(ip)
  print host_list
  
 
def copy_scp(ip):
  source="/home/mastere/ip"
  dst="~/Desktop"      
  print ip   
  remote_host="identifiant@"+ip
  if ip =='192.168.4.229':
    print "salut"
    subprocess.call('scp',source,":".join([remote_host,dst]))
        
         
def admincheck():
  if checkip()==admin_ip:
     print "admin privileges"



def checkip():

  ip=commands.getoutput("ifconfig").split("\n")[1].split()[1][5:]
  return ip
  
def chk():
  
  #print uid
  #print gid
  if uid == 0: 
    print "ip=",checkip()
    
    
  else:
        print "not the root"

chk()
admincheck()  
portscan()


  
