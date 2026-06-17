#!/usr/bin/env python3

import json
import os
import sys

import requests


def get_api_url():
    return os.environ.get("GROK_API_URL", "https://api.grok.ai/v1/generate")


def get_api_key():
    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        raise SystemExit("Error: Set GROK_API_KEY environment variable")
    return api_key


def test_grok(prompt):
    url = get_api_url()
    headers = {
        "Authorization": f"Bearer {get_api_key()}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "max_tokens": 64,
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Write a short greeting from Grok."
    result = test_grok(prompt)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
