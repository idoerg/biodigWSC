package BioDIGAPI;

import java.util.Arrays;
import java.util.Date;

import javax.ws.rs.core.MultivaluedMap;
import com.sun.jersey.core.util.MultivaluedMapImpl;

public class TagGroupQuery{
	MultivaluedMap params;
	private int ID,imageID;
	private String name,user;
	private Date lastModified, dateCreated;
	private boolean isPrivate;

	public TagGroupQuery(){
		this.params = new MultivaluedMapImpl();
		this.ID = -1;
		this.imageID = -1;
		this.lastModified = null;
		this.dateCreated = null;
		this.name = "";
		this.user = "";
		this.isPrivate = false;
	}

	public void addID(int ID) {
		this.ID = ID;
	}

	public void addImageID(int imageID) {
		this.imageID = imageID;
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
		if(ID != -1)
			params.add("ID", Integer.toString(ID));
		if(imageID != -1)
			params.add("imageID", Integer.toString(imageID));
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