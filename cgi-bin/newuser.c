#include <stdio.h>
#include <string.h>

int main()
{
	char raw_data[400],nameIn[200], passwordIn[200],garbage[100];

	fgets(raw_data,400,stdin);
	int len = strlen(raw_data);
	int i;
	for(i=0; i<len; i++)
	{
		if(raw_data[i]=='='||raw_data[i]=='&')
		{
			raw_data[i]=' ';
		}
		   
	}

	char* temp=strdup(raw_data);
	sscanf(temp, "%s %s %s %s", garbage, nameIn, garbage, passwordIn);

	FILE *fp;

	fp = fopen("../members.ssv","rt"); //fp: file pointer

	if (fp == NULL) {
		printf("Error: Cannot find the SSV file.\n");
		return -1;
	}

	int accountExists = 0;

	while(!feof(fp)){
		char str[400], name[200], password[200];
		fgets(str, 400, fp); //get a line from SSV
		sscanf(str,"%s %s",name,password);
		
		if (strcmp(nameIn, name)==0){
			accountExists=1;
			break;
		}
	}

	fclose(fp);

	printf("%s%c%c\n\n","Content-Type: text/html;charset=iso-8859-1",13,10);

	if(accountExists){
		printf("<html><head><title>User Name Already Exists - Otaku High Five!</title></head>\n");
		printf("<body bgcolor=\"white\" text=\"black\" background=\"../background.jpg\">\n");
		printf("<center><h1 style=\"color:#FFB873; font-family:COURIER NEW; font-size:50;\">THAT USER NAME HAS ALREADY BEEN USED.</h1><center>\n");
		printf("<img src=\"../doge_r.gif\"/>\n");
		printf("<p style =\"color:#333399; font-family:PERPETUA;\">Please try again!</p>\n");

		printf("</table><h1 style =\"color:#330066; font-family:PERPETUA;\">Menu</h1>\n");
		printf("<table width=\"60%%\"><tr><td align=\"right\"><input type =\"button\" style=\"width: 200px;\" value =\"Existing User Login\" onclick =\"location.href ='../login.html'\"/></td>\n");
		printf("<td align=\"center\" width=\"210px\"><input type =\"button\" style=\"width: 200px;\" value =\"Back to Create Account\" onclick =\"location.href ='../createAccount.html'\"/></td>\n");
		printf("<td align=\"left\"><input type =\"submit\" style=\"width: 200px;\" value =\"Back to Home Page\" onclick =\"location.href ='../index.html'\"/></td></tr></table>\n");

		printf("<p><img src=\"../coverphoto.jpg\" width=\"80%%\" height=\"35%%\"/></p></center></body></html>\n");

		return 0;	
	}

	fp =fopen("../members.ssv","at");
	fprintf(fp,"%s %s\n",nameIn, passwordIn);
	fclose(fp);

	printf("<html><head><title>Account Created Successfully - Otaku High Five!</title></head>\n");
	printf("<body bgcolor=\"white\" text=\"black\" background=\"../background.jpg\">\n");
	printf("<center><h1 style=\"color:#FFB873; font-family:COURIER NEW; font-size:50;\">YOUR USER NAME AND PASSWORD HAS BEEN ACCEPTED.</h1><center>\n");
	printf("<img src=\"../doge_r.gif\"/>\n");
	printf("<p style =\"color:#333399; font-family:PERPETUA;\">You can now login!</p>\n");

	printf("</table><h1 style =\"color:#330066; font-family:PERPETUA;\">Menu</h1>\n");
	printf("<table width=\"60%%\"><tr><td align=\"right\"><input type =\"button\" style=\"width: 200px;\" value =\"Go to Login Page\" onclick =\"location.href ='../login.html'\"/></td>\n");
	printf("<td align=\"left\"><input type =\"submit\" style=\"width: 200px;\" value =\"Back to Home Page\" onclick =\"location.href ='../index.html'\"/></td></tr></table>\n");

	printf("<p><img src=\"../coverphoto.jpg\" width=\"80%%\" height=\"35%%\"/></p></center></body></html>\n");
	
	return 1;
}
