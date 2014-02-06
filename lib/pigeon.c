#include <Python.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

char *host;
int portno;
int sockfd;
int n;

static PyObject* pInit(PyObject* self,PyObject *args)
{
	portno=25;
	if(!PyArg_ParseTuple(args,"s",&host)){
		return Py_BuildValue("s","Error host");
	}
	struct sockaddr_in serv_addr; //store server addr
	sockfd = socket(AF_INET, SOCK_STREAM, 0); //create the socket file desc
	if (sockfd < 0) 
        	return Py_BuildValue("s","Error opening socket");
	bzero((char *) &serv_addr, sizeof(serv_addr)); //make it zero
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(portno);
	//convert server address to binary format
    	if(inet_pton(AF_INET, host, &serv_addr.sin_addr)<=0)
    		return Py_BuildValue("s","inet_pton error occured");
	//try connecting to server
    	if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) 
        	return Py_BuildValue("s","Error occured during connection");
	char buffer[256];
	bzero(buffer,256);
	n = read(sockfd,buffer,255);
    	if (n < 0) 
       		return Py_BuildValue("s","Error reading from socket");
    	return Py_BuildValue("s",buffer);
}

static char pInit_docs[] =
    	"pigeon( ): Initialize with mailserver address!!\n";

static PyObject* sayHello(PyObject* self,PyObject *args){
	char *dn;
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	if(!PyArg_ParseTuple(args,"s",&dn)){
		return Py_BuildValue("s","Error:: domain name required");
	}
	char *hello = malloc(5+strlen(dn)+2);
	char command[] = "ehlo ";
	strcpy(hello,command);
	strcat(hello,dn);
	strcat(hello,"\n");
	n = write(sockfd,hello,strlen(hello));
    	if (n < 0) 
    	    	return Py_BuildValue("s","Error writing to socket");
	char buffer[256];
	bzero(buffer,256);
    	n = read(sockfd,buffer,255);
	if (n < 0)
		return Py_BuildValue("s","Error writing to socket");
	return Py_BuildValue("s",buffer);
	Py_RETURN_NONE;
}


static char sayHello_docs[]=
	"sayHello():say hello to the mailserver\n";

static PyObject* msgFrom(PyObject* self,PyObject *args){
	char *sendto;
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	if(!PyArg_ParseTuple(args,"s",&sendto)){
		return Py_BuildValue("s","Error:: email address required");
	}
	char command[] = "mail from:";
	char *msgFr = malloc(10+strlen(sendto)+2);
	strcpy(msgFr,command);
	strcat(msgFr,sendto);
	strcat(msgFr,"\n");
	n = write(sockfd,msgFr,strlen(msgFr));
	if ( n< 0)
		return Py_BuildValue("s","Error writing to socket");
	char buffer[256];
	bzero(buffer,256);
	n = read(sockfd,buffer,255);
	if ( n<0)
		return Py_BuildValue("s","Error reading from socket");
	return Py_BuildValue("s",buffer);
}

static char msgFrom_docs[] = 
	"msgFrom():specify the mail address to send the mail\n";

static PyObject* rcptTo(PyObject* self,PyObject *args){
	char *rcpt;
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	if(!PyArg_ParseTuple(args,"s",&rcpt)){
		return Py_BuildValue("s","Error:: email address required");
	}
	char command[] = "rcpt to:";
	char *rct = malloc(8+strlen(rcpt)+2);
	strcpy(rct,command);
	strcat(rct,rcpt);
	strcat(rct,"\n");
	n = write(sockfd,rct,strlen(rct));
	if ( n< 0)
		return Py_BuildValue("s","Error writing to socket");
	char buffer[256];
	bzero(buffer,256);
	n = read(sockfd,buffer,255);
	if ( n<0)
		return Py_BuildValue("s","Error reading from socket");
	return Py_BuildValue("s",buffer);	
}

static char rcptTo_docs[] = 
	"rcptTo():enter recipients name\n";


static PyObject* beginData(PyObject* self){
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	char command[] = "data\n";
	n = write(sockfd,command,strlen(command));
	if ( n< 0)
		return Py_BuildValue("s","Error writing to socket");
	char buffer[256];
	bzero(buffer,256);
	n = read(sockfd,buffer,255);
	if ( n<0)
		return Py_BuildValue("s","Error reading from socket");
	return Py_BuildValue("s",buffer);
}

static char beginData_docs[] =
	"beginData():start writing data after auth\n";

static PyObject* writeData(PyObject* self,PyObject *args){
	char *data;
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	if(!PyArg_ParseTuple(args,"s",&data)){
		return Py_BuildValue("s","Error:: email address required");
	}
	char *sdata=malloc(strlen(data)+1);
	strcpy(sdata,data);
	strcat(sdata,"\n");
	n = write(sockfd,sdata,strlen(sdata));
	if ( n< 0)
		return Py_BuildValue("s","Error writing to socket");
	Py_RETURN_NONE;
}
	
static char writeData_docs[] = 
	"writeData(data):data to be written in mail body\n";

static PyObject* sendMsg(PyObject* self){
	if(sockfd < 0)
		return Py_BuildValue("s","Error :Initialize first");
	char end[] = ".\n";
	n = write(sockfd,end,strlen(end));
	if ( n< 0)
		return Py_BuildValue("s","Error writing to socket");
	char buffer[256];
	bzero(buffer,256);
	n = read(sockfd,buffer,255);
	if ( n<0)
		return Py_BuildValue("s","Error reading from socket");
	return Py_BuildValue("s",buffer);
}	

static char sendMsg_docs[] = 
	"sendMsg():ends data and send message\n";

static PyMethodDef pInit_funcs[] = {
    	{"pigeon", (PyCFunction)pInit, 
     	METH_VARARGS, pInit_docs},
	{"sayHello",(PyCFunction)sayHello,
	METH_VARARGS,sayHello_docs},
	{"msgFrom",(PyCFunction)msgFrom,
	METH_VARARGS,msgFrom_docs},
	{"rcptTo",(PyCFunction)rcptTo,
	METH_VARARGS,rcptTo_docs},
	{"beginData",(PyCFunction)beginData,
	METH_NOARGS,beginData_docs},
	{"writeData",(PyCFunction)writeData,
	METH_VARARGS,writeData_docs},
	{"sendMsg",(PyCFunction)sendMsg,
	METH_NOARGS,sendMsg_docs},
    	{NULL}
};


void initpigeon(void)
{
    	Py_InitModule3("pigeon", pInit_funcs, //has to be module name
                   "Telnet Mail Module!");
}
