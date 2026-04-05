#!/bin/sh
set -e

# clear ready flag
rm -f /tmp/ready

ollama serve &

# start ollama, wait for it to serve
echo "Starting Ollama..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 1
done

# all the models to install
MODELS="mistral-small"

# pull and install models, or skip if they're present
for MODEL in $MODELS; do
  if ! ollama list | grep -q "$MODEL"; then
    echo "⚡️ Pulling model: $MODEL"
    ollama pull "$MODEL"
  else
    echo "⛳️ Model '$MODEL' already present."
  fi
done

for MODEL in $MODELS; do
  echo "💡 Preloading model: $MODEL ..."
  ollama run "$MODEL" "Hello, are you ready?" --keep-alive 1h > /dev/null 2>&1 &
  echo "✅ Model '$MODEL' successfully preloaded and kept alive."
done

if command -v nvidia-smi &> /dev/null; then
  echo "✅ GPU detected, enabling acceleration"
  export OLLAMA_GPU=1
else
  echo "⚙️ No GPU found, running on CPU"
  export OLLAMA_GPU=0
fi

# set container as ready
touch /tmp/ready

echo "🎯 Ollama is fully ready. Models loaded into memory."

# start nginx
nginx -g "daemon off;"