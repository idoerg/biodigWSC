package geneLinks;

import javax.ws.rs.core.MultivaluedMap;

import com.sun.jersey.core.util.MultivaluedMapImpl;

//Class that is used to build a geneLink object
public class geneLinkQuery 
{

	//Empty variables to be filled later by the user as needed
	MultivaluedMap params;
	String name,uniquename;
	int organismId,tagId;

	//Creates an empty instance of all the editable fields for the image JSON PUT and POST operations
	public geneLinkQuery()
	{
		this.params = new MultivaluedMapImpl();
		this.name = "";
		this.uniquename = "";
		this.organismId = -1;

	}
	
	//Edits the Alternative Text for the GeneLink
	public void addAltText(String altText) {
		this.name = altText;
	}

	//Edits the description of the GeneLink
	public void addDescription(String description) {
		this.uniquename = description;
	}
	
	//Changes the Organism ID for this GeneLink
	public void addOrganismId(int organismId) {
		this.organismId = organismId;
	}
	
	//Adds the Tag so that the operation of PUT, GET, and DELETE can succeed.
	public void addTagId(int tagId){
		this.tagId = tagId;
	}

	//Creates a Map to add to the API calls if they have meet the requirements of being activated by the user.
	public MultivaluedMap getQuery() {
		if(!name.equals(""))
			params.add("name", name);
		if(!uniquename.equals(""))
			params.add("user", uniquename);
		if(organismId >-1)
			params.add("organismid", organismId);
		if(tagId >-1)
			params.add("tagId", tagId);
		System.out.println(params.toString());

		return params;
	}




}
