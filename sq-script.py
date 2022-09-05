#!/usr/bin/env python3
# Squadcast
import os
import json
import urllib.request


def form_payload(hostName="", hostState="", hostOutput="", notifyDateTime="", notificationType="", serviceDesc="", serviceOutput="", serviceState="", source="", hostNotifNumber="", serviceNotifNumber=""):

    payload_rep = {"hostname": hostName, "hostState": hostState, "hostOutput": hostOutput, "notifyDateTime": notifyDateTime, "notificationType": notificationType, "serviceDesc": serviceDesc,
                   "serviceOutput": serviceOutput, "serviceState": serviceState, "source": source, "hostNotifNumber": hostNotifNumber, "serviceNotifNumber": serviceNotifNumber}
    return payload_rep


def post_to_url(url, payload):

    try:
        headers={
        'User-Agent': 'squadcast',
        "Content-Type": "application/json"
        }
        req = urllib.request.Request(url, data=bytes(json.dumps(payload),"utf-8"),headers=headers)
        resp = urllib.request.urlopen(req)
        if resp.status > 299:
            print("[sq-checkmk] Request failed with status code %s : %s" %
                  (resp.status, resp.read()))
    except urllib.request.URLError as e:
        if e.code >= 400 and e.code < 500:
            print("[sq-checkmk] Some error occured while processing the event")


if __name__ == "__main__":

    print("Sending data to squadcast")
    url = source = hostName = hostState = hostOutput = hostNotifNumber = notifyDateTime = notificationType = serviceDesc = serviceOutput = serviceState = serviceNotifNumber = ""
    url = os.environ.get("NOTIFY_PARAMETER_1")
    source = os.environ.get("NOTIFY_WHAT")
    hostName = os.environ.get("NOTIFY_HOSTNAME")
    hostState = os.environ.get("NOTIFY_HOSTSTATE")
    hostOutput = os.environ.get("NOTIFY_HOSTOUTPUT")
    hostNotifNumber = os.environ.get("NOTIFY_HOSTNOTIFICATIONNUMBER")
    hostAddress = os.environ.get("NOTIFY_HOSTADDRESS")
    notifyDateTime = os.environ.get("NOTIFY_SHORTDATETIME")
    notificationType = os.environ.get("NOTIFY_NOTIFICATIONTYPE")
    if source == "SERVICE":
        serviceDesc = os.environ.get("NOTIFY_SERVICEDESC")
        serviceOutput = os.environ.get("NOTIFY_SERVICEOUTPUT")
        serviceState = os.environ.get("NOTIFY_SERVICESTATE")
        serviceNotifNumber = os.environ.get("NOTIFY_SERVICENOTIFICATIONNUMBER")

    post_to_url(url, form_payload(hostName, hostState, hostOutput, notifyDateTime, notificationType,
                                  serviceDesc, serviceOutput, serviceState, source, hostNotifNumber, serviceNotifNumber))
    print("Done.")
