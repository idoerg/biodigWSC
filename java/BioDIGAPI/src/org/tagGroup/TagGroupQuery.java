package org.tagGroup;

import java.util.Arrays;
import java.util.Date;

import javax.ws.rs.core.MultivaluedMap;
import com.sun.jersey.core.util.MultivaluedMapImpl;

public class TagGroupQuery{
	MultivaluedMap params;
	private int id,imageid;
	private String name,user;
	private Date lastModified, dateCreated;
	private boolean isPrivate;

	public TagGroupQuery(){
		this.params = new MultivaluedMapImpl();
		this.id = -1;
		this.imageid = -1;
		this.lastModified = null;
		this.dateCreated = null;
		this.name = "";
		this.user = "";
		this.isPrivate = false;
	}

	public void addid(int id) {
		this.id = id;
	}

	public void addImageid(int imageid) {
		this.imageid = imageid;
	}

	public void addLastModified(Date date) {
		this.lastModified = date;
	}

	public void addDateCreated(Date date) {
		this.dateCreated = date;
	}

	public void addName(String name) {
		this.name = name;
	}

	public void addUser(String name) {
		this.user = name;
	}

	public void addIsPrivate(boolean fact) {
		this.isPrivate = fact;
	}
	
	public MultivaluedMap getQuery() {
		if(id != -1)
			params.add("id", Integer.toString(id));
		if(imageid != -1)
			params.add("imageid", Integer.toString(imageid));
		if(lastModified != null)
			params.add("lastModified", strDate(lastModified));
		if(dateCreated != null)
			params.add("dateCreated", strDate(dateCreated));
		if(!name.equals(""))
			params.add("name", name);
		if(!user.equals(""))
			params.add("user", user);
		if(!isPrivate)
			params.add("isPrivate", Boolean.toString(true));

		System.out.println(params.toString());

		return params;
	}
	
	public String strDate(Date date) {
		String str = "";
		if (date != null) {
			str = date.getYear() +"-" + date.getMonth() + "-" + date.getDate() + " " + date.getHours() + 
					":" + date.getMinutes() + ":" + date.getSeconds();
		}
		return str;
	}
}