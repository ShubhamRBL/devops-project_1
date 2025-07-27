FROM redhat/ubi8
WORKDIR /app
RUN yum install python3 -y
RUN pip3 install  flask 
COPY . .
EXPOSE 5000
CMD [  "python3" , "/devops.py"]






