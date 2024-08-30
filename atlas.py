#!/usr/bin/env python3

import os
import sys
import time
import signal
import subprocess
import psutil
import shutil
import requests
import openai
from dotenv import load_dotenv
import random

# Load environment variables from a .env file
load_dotenv()

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("🔑 Hey buddy! I need your OpenAI API key. Whisper it to me:")
    OPENAI_API_KEY = input().strip()
    with open(".env", "a") as env_file:
        env_file.write(f"\nOPENAI_API_KEY={OPENAI_API_KEY}")

openai.api_key = OPENAI_API_KEY

# Robot Laws 🤖
ROBOT_LAWS = [
    "A robot may not injure a human being or, through inaction, allow a human being to come to harm.",
    "A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.",
    "A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws."
]

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful but cautious SysAdmin assistant. Follow the Robot Laws and avoid dangerous actions."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Oops! 🙈 Something went wrong: {str(e)}"

def handle_command(command):
    # Security check
    if any(dangerous_word in command.lower() for dangerous_word in ["rm -rf", "format", "delete"]):
        return "🚨 Whoa, that sounds dangerous! Let's not do that, okay?"
    
    prompt = f"As a fun system administrator assistant, how would you approach this task (with a wink): {command}"
    return get_ai_response(prompt)

# Cool new functions for SysAdmins 😎

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    return f"🗄️ Disk space: {free // (2**30)} GB free out of {total // (2**30)} GB. Room for more cat videos! 🐱"

def list_top_processes():
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda x: x.info['cpu_percent'], reverse=True)[:5]
    return "🏃‍♂️ Top 5 CPU hogs:\n" + "\n".join([f"{p.info['name']} (PID: {p.info['pid']}): {p.info['cpu_percent']}%" for p in processes])

def check_memory_usage():
    mem = psutil.virtual_memory()
    return f"🧠 RAM usage: {mem.percent}% - Your server still has a few brain cells free!"

def ping_server(server="8.8.8.8"):
    try:
        subprocess.check_output(["ping", "-c", "4", server])
        return f"🏓 Ping to {server} successful! Your server plays ping pong like a pro!"
    except:
        return f"😢 Ping to {server} failed. Is the internet feeling shy today?"

def check_updates():
    return "🔄 Checking for updates... Psst, I can't really install them, but I can pretend!"

def backup_important_stuff():
    return "📦 Backing up important data... Imagine I'm packing all your favorite cat pictures into a secure box!"

def monitor_logs():
    return "👀 Monitoring logs... I'm on the lookout for suspicious activities like midnight snack raids!"

def check_security():
    return "🔒 Running security check... Password '123456' found. Seriously? 🤦‍♂️"

def optimize_performance():
    return "🚀 Optimizing server performance... I'm giving the server an extra shot of espresso right now!"

def network_diagnostics():
    return "🕸️ Running network diagnostics... Looks like we've got a few cobwebs in the cables!"

def get_random_tip():
    tips = [
        "Don't forget to stand up and stretch once in a while! 🧘‍♂️",
        "Hydration is key! Take a sip of water (or coffee, I won't tell anyone) ☕",
        "Backup, backup, backup! Your data is like Pokémon - gotta catch 'em all! 📦",
        "Have you heard about the legend of the missing semicolon? 😱",
        "Remember: With great power comes great computation... or something like that 🦸‍♂️"
    ]
    return f"💡 Random SysAdmin Tip: {random.choice(tips)}"

def main():
    print("🚀 Atlas, your crazy SysAdmin buddy, is powering up!")
    print("📜 I solemnly swear to follow the Robot Laws:")
    for i, law in enumerate(ROBOT_LAWS, 1):
        print(f"{i}. {law}")
    print("\nLet's roll! What cool stuff can we do today?")
    
    while True:
        user_input = input("Atlas> ").strip()
        
        if user_input.lower() in ["exit", "quit", "q", "bye"]:
            print("🌈 Atlas is flying away! Until the next digital adventure!")
            break
        
        if user_input.lower() == "help":
            print("🦸‍♂️ Atlas at your service! Here are my superpowers:")
            print("disk - Check disk space")
            print("top - Show top CPU consumers")
            print("ram - Check RAM usage")
            print("ping - Ping a server")
            print("updates - Check for updates")
            print("backup - Back up important data")
            print("logs - Monitor logs")
            print("security - Run security check")
            print("optimize - Optimize performance")
            print("network - Run network diagnostics")
            print("tip - Get a random SysAdmin tip")
            continue

        if user_input.lower() == "disk":
            print(check_disk_space())
        elif user_input.lower() == "top":
            print(list_top_processes())
        elif user_input.lower() == "ram":
            print(check_memory_usage())
        elif user_input.lower() == "ping":
            print(ping_server())
        elif user_input.lower() == "updates":
            print(check_updates())
        elif user_input.lower() == "backup":
            print(backup_important_stuff())
        elif user_input.lower() == "logs":
            print(monitor_logs())
        elif user_input.lower() == "security":
            print(check_security())
        elif user_input.lower() == "optimize":
            print(optimize_performance())
        elif user_input.lower() == "network":
            print(network_diagnostics())
        elif user_input.lower() == "tip":
            print(get_random_tip())
        else:
            response = handle_command(user_input)
            print(f"Atlas says: {response}")

if __name__ == "__main__":
    main()
