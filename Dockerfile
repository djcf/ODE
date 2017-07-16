FROM python:3.4-slim
WORKDIR /var/ode
RUN apt-get update && apt-get -y --no-install-recommends install git make gcc build-essential && mkdir /data && \
	pip install --upgrade pip && \
	git clone https://github.com/djcf/ODE.git /var/ode && \
	make develop && \
	apt-get -y remove gcc git python3-dev build-essential && \ 
	apt-get -y clean && \
	apt-get -y autoremove && \
	rm -rf /var/lib/apt/lists/* && \
	adduser --system --no-create-home --group --shell=/bin/false ode && usermod -a -G www-data ode
CMD ["make", "serve"]
HEALTHCHECK CMD curl --fail http://localhost:6543/ || exit 1
EXPOSE "6543"
USER ode
VOLUME /data