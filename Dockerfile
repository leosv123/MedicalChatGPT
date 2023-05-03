From continuumio/miniconda3

RUN apt-get update && apt-get install -y wget build-essential apt-transport-https ca-certificates && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils gnupg2 curl

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    vim \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

RUN conda create -n chatenv python=3.9
RUN apt-get update && apt-get install -y cmake
RUN mkdir /app
WORKDIR /app

COPY [ "*", "./" ]
RUN /bin/bash -c "source activate chatenv && pip install -r requirements.txt"

COPY . .


CMD ["conda","run","--no-capture-output","-n","chatenv","uvicorn","main_api:app","--host","0.0.0.0","--port","8020"]
