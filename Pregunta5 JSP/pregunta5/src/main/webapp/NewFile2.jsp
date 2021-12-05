<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
<%	String se = "";
	String numero = request.getParameter("nro");
	int a, b, limite, i, auxiliar;
	limite = Integer.parseInt(numero); 
	a = 0;
	b = 1; 
	for (i = 0; i < limite; i++)  
	{
	    auxiliar = a;
	    a = b; 
	    b = auxiliar + a;
	    se = se + a + ", ";
	}
%>
</head>
<body>
<h4>La serie generada es : <% out.print(se); %> </h4>


</html>