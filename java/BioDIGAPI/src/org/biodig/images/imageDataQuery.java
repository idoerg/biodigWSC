package images;

import java.io.File;
import java.util.List;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import com.sun.jersey.core.util.MultivaluedMapImpl;
import com.sun.jersey.multipart.FormDataMultiPart;

public class imageDataQuery 
{

	//Empty variables to be filled later by the user as needed
	FormDataMultiPart params;
	private String altText, description;
	private File file;
	private List<Organism> organisms;
	private int id;

	//Creates an empty instance of all the editable fields for the image JSON PUT and POST operations
	public imageDataQuery()
	{
		this.params = new  FormDataMultiPart();
		this.altText = "";
		this.description = "";
		this.organisms = null;
		this.id = -1;
		this.file = null;
	}

	//Edits the alternative text assoicated with an image.
	public void addAltText(String altText) {
		this.altText = altText;
	}

	//Edits the description attached to the images.
	public void addDescription(String description) {
		this.description = description;
	}
	
	//Edits the list of organisms associated with the image.
	public void addOrganisms(List<Organism> organisms) {
		this.organisms = organisms;
	}
	
	//Edits the filepath in which you are using for the POST operation.
	public void addFile(File imgFile) {
		this.file = imgFile;
	}

	//Used in PUT, GET, and DELETE. Identifies which image to do the three opeations on.
	public void addId(int id){
		this.id = id;
	}
	
	//Note: The get methods for the values in this class are at the moment being used for POST image, since it is a pain
	//in the arse and doesn't want to play nice with query. I had to use a non-conforming method to get it to post.
	
	public String getAltText() {
		return altText;
	}

	public String getDescription() {
		return description;
	}

	public File getFile() {
		return file;
	}

	public List<Organism> getOrganisms() {
		return organisms;
	}

	public int getId() {
		return id;
	}
	
	//Multimap that will add parameters based on which one is active.
	public  FormDataMultiPart getQuery() {
		if(!altText.equals(""))
			params.field("name", altText);
		if(!description.equals(""))
			params.field("user", description);
		if(organisms != null)
			params.field("organisms", organisms.toString());
		if(file != null)
			params.field("image", file, MediaType.MULTIPART_FORM_DATA_TYPE);
		if(id >-1)
			params.field("id", Integer.toString(id));
		System.out.println(params.toString());

		return params;
	}



}