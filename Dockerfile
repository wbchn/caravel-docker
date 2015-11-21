FROM python:2.7.10

# Install panoramix
RUN pip install panoramix && \
    mkdir /panoramix

# Create an admin user env
ENV username admin
ENV password changeme
ENV firstname admin
ENV lastname sample
ENV email user@sample.com

# Add server script and default config
ADD run.sh /run.sh
ADD panoramix/* /panoramix

# Start the web server foreground
CMD [ "/bin/bash", "/run.sh" ]
