package geneLinks;

public class geneLinkData 
{
	
	//Constructor without caching
	public geneLinkData(String name, int organismId,
			String uniquename) {
		super();
		this.name = name;
		this.organismId = organismId;
		this.uniquename = uniquename;
	}
	
	//Constructor without caching
		public geneLinkData(String name, int organismId,
				String uniquename, boolean cachingFlag) {
			super();
			this.name = name;
			this.organismId = organismId;
			this.uniquename = uniquename;
			this.cachingFlag = cachingFlag;
		}
	//Variables Used
	private String name;
	private int tagId;
	private int organismId;
	private String uniquename;
	private int id;
	private String user;
	private boolean cachingFlag;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getTagId() {
		return tagId;
	}
	public void setTagId(int tagId) {
		this.tagId = tagId;
	}
	public int getOrganismId() {
		return organismId;
	}
	public void setOrganismId(int organismId) {
		this.organismId = organismId;
	}
	public String getUniquename() {
		return uniquename;
	}
	public void setUniquename(String uniquename) {
		this.uniquename = uniquename;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getUser() {
		return user;
	}
	public void setUser(String user) {
		this.user = user;
	}
	
	//Toggles the flag for caching to be false if true, and true if false
			public void changeCaching()
			{
				if(cachingFlag == false)
				{
					cachingFlag = true;
				}
				if(cachingFlag == true)
				{
					cachingFlag = false;
				}
			}
	
	@Override
	public String toString() {
		return "geneLinkData \n[name=" + name + ",\n tagId=" + tagId
				+ ",\n organismId=" + organismId + ",\n uniquename=" + uniquename
				+ ",\n id=" + id + ",\n user=" + user + "]";
	}

}
