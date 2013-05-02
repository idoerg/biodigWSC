package org.biodig.genelinks;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.UriBuilder;
import javax.xml.ws.http.HTTPException;

import com.google.gson.Gson;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.UniformInterfaceException;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import com.sun.jersey.multipart.FormDataMultiPart;

public class geneLinksMethods 
{

	public static void main(String[] args) 
	{

	}

	public static void getGeneLinkInfo(String geneLinkId) 
	{
		try
		{
		ClientConfig config = new DefaultClientConfig();
		Client client = Client.create(config);
		WebResource service = client.resource(UriBuilder.fromUri("http://wan1.mbi.muohio.edu/dome/api/geneLinks?id="+geneLinkId).build());
		ClientResponse response = service.accept(MediaType.TEXT_HTML).get(ClientResponse.class);
	//---Used for debugging purposes to check the status of the Get call----
		//System.out.println(response.toString());

		String imageMetaData = service.accept(MediaType.APPLICATION_JSON).get(String.class);
		//System.out.println(imageMetaData);
		
		//Creation of objects to parse the raw JSON data
		geneLinkData geneLink = new Gson().fromJson(imageMetaData, geneLinkData.class);

		System.out.println(geneLink.toString());
		}
		catch(UniformInterfaceException e)
		{
			System.out.println("Your request cannot be processed, try entering a valid image Id.");
			e.printStackTrace();
		}
	}
	
	static public void addGeneLink(geneLinkData feature, String tagId)
	{
		try
		{
		ClientConfig cc = new DefaultClientConfig();
        Client client = Client.create(cc);
        WebResource resource = client.resource("http://192.168.142.128/api/geneLinks");
		//Post
        FormDataMultiPart form = new FormDataMultiPart();
        form.field("feature" , new Gson().toJson(feature));
        form.field("tagId", tagId);
	    ClientResponse response = resource.type(MediaType.MULTIPART_FORM_DATA).post(ClientResponse.class, form);
	    System.out.println(response.toString());
		}
		catch(HTTPException e)
		{
			System.out.println("Website Not Reachable.");
		}
	}
}
