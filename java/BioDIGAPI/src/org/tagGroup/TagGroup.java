package BioDIGAPI;
import java.util.Date;
import com.google.gson.Gson;

public class TagGroup {
	private int ID; 
	private int imageID;
	private Date lastModified;
	private Date dateCreated;
	private String name;
	private String user;
	private boolean isPrivate;
	
	public TagGroup (int ID, int imageID, Date lastModified, Date dateCreated, String name, String user, boolean isPrivate) {
		this.ID = ID;
		this.imageID = imageID;
		this.lastModified = lastModified;
		this.dateCreated = dateCreated;
		this.name = name;
		this.user = user;
		this.isPrivate = isPrivate;
	}
	
	public String toString() {
		@SuppressWarnings("deprecation")
		String str = "{\"name\": \"" + name + "\", \"lastModified\": \"" + strDate(lastModified) + "\", \"imageID\": " + imageID + ", \"user\": \"" + user + 
				"\", \"isPrivate\": " + isPrivate + ", \"dateCreated\": \"" + strDate(dateCreated) + "\", \"id\": " + ID + "}";
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
	
	public int getImageID() {
		return imageID;
	}

	public void setImageID(int imageID) {
		this.imageID = imageID;
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
	
	public int getID () {
		return ID;
	}

	public void setID (int ID) {
		this.ID = ID;
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