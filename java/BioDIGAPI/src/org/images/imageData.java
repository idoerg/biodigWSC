package images;

import java.util.List;

//Main class that holds the structure of an image object
public class imageData
	{
	
	//internal private variables
			private String altText;
			private String description;
			private List<Organism> organisms;
			private String url;
			private String thumbnail;
			private String uploadDate;
			private int id;
			private String uploadedBy;
			
			//flag of caching, default to false
			private boolean cachingFlag = false;

	
	//Constructor without cache flag
		public imageData(String altText, String description,List<Organism> organisms)
	{
		super();
		this.altText = altText;
		this.description = description;
		this.organisms = organisms;

	}
		
	//Constructor with cache flag
		public imageData(String altText, String description,List<Organism> organisms, boolean cachingFlag)
			{
				super();
				this.altText = altText;
				this.description = description;
				this.organisms = organisms;
				this.cachingFlag = cachingFlag;
			}
		
		public imageData()
		{
			
		}

		public String getAltText() {
			return altText;
		}

		public void setAltText(String altText) {
			this.altText = altText;
		}

		public String getDescription() {
			return description;
		}

		public void setDescription(String description) {
			this.description = description;
		}

		public String getUrl() {
			return url;
		}

		public void setUrl(String url) {
			this.url = url;
		}

		public String getThumbnail() {
			return thumbnail;
		}

		public void setThumbnail(String thumbnail) {
			this.thumbnail = thumbnail;
		}

		public String getUploadDate() {
			return uploadDate;
		}

		public void setUploadDate(String uploadDate) {
			this.uploadDate = uploadDate;
		}

		public int getId() {
			return id;
		}

		public void setId(int id) {
			this.id = id;
		}

		public String getUploadedBy() {
			return uploadedBy;
		}

		public void setUploadedBy(String uploadedBy) {
			this.uploadedBy = uploadedBy;
		}

		public List<Organism> getOrganisms() {
			return organisms;
		}

		public void setOrganisms(List<Organism> org) {
			this.organisms = org;
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
			return 

					"imageData: \n [altText=" + altText + ",\n description="
					+ description + ",\n org=" + organisms + ",\n url=" + url
					+ ",\n thumbnail=" + thumbnail + ",\n uploadDate=" + uploadDate
					+ ",\n id=" + id + ",\n uploadedBy=" + uploadedBy + "]";
			
		}	
}