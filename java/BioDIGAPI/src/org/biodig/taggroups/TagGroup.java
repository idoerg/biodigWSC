package org.biodig.taggroups;
import java.util.Date;

public class TagGroup {
	private int id; 
	private int imageid;
	private Date lastModified;
	private Date dateCreated;
	private String name;
	private String user;
	private boolean isPrivate;
	
	public TagGroup (int id, int imageid, Date lastModified, Date dateCreated, String name, String user, boolean isPrivate) {
		this.id = id;
		this.imageid = imageid;
		this.lastModified = lastModified;
		this.dateCreated = dateCreated;
		this.name = name;
		this.user = user;
		this.isPrivate = isPrivate;
	}
	
	public String toString() {
		String str = "{\"name\": \"" + name + "\", \"lastModified\": \"" + strDate(lastModified) + "\", \"imageid\": " + imageid + ", \"user\": \"" + user + 
				"\", \"isPrivate\": " + isPrivate + ", \"dateCreated\": \"" + strDate(dateCreated) + "\", \"id\": " + id + "}";
		return str;
	}
	
	public String strDate(Date date) {
		String str = "";
		if (date != null) {
			str = date.getYear() +"-" + date.getMonth() + "-" + date.getDate() + " " + date.getHours() + 
					":" + date.getMinutes() + ":" + date.getSeconds();
		}
		return str;
	}
	
	public int getImageid() {
		return imageid;
	}

	public void setImageid(int imageid) {
		this.imageid = imageid;
	}

	public String getUser() {
		return user;
	}

	public void setUser(String user) {
		this.user = user;
	}

	public boolean isPrivate() {
		return isPrivate;
	}

	public void setPrivate(boolean isPrivate) {
		this.isPrivate = isPrivate;
	}
	
	public int getid () {
		return id;
	}

	public void setid (int id) {
		this.id = id;
	}
	
	public Date getLastModified () {
		return lastModified;
	}

	public void setLastModified (Date lastModified) {
		this.lastModified = lastModified;
	}

	public Date getDateCreated () {
		return dateCreated;
	}

	public void setDateCreated (Date dateCreated) {
		this.dateCreated = dateCreated;
	}

	public String getName () {
		return name;
	}

	public void setName (String name) {
		this.name = name;
	}
}