package BioDIGAPI;

import java.util.Arrays;

public class geneLinks {
	private int id,tagId,organismId;
	private String uniquename,name;
	
	/*
	 * Constructor 
	 */
	public geneLinks (int id, int tagId, String uniquename, String name, int organismId) {
		this.id = id;
		this.tagId = tagId;
		this.uniquename = uniquename;
		this.name = name;
		this.organismId = organismId;
	}

	/**
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * @return the tagId
	 */
	public int getTagId() {
		return tagId;
	}

	/**
	 * @param tagId the tagId to set
	 */
	public void setTagId(int tagId) {
		this.tagId = tagId;
	}

	/**
	 * @return the organismId
	 */
	public int getOrganismId() {
		return organismId;
	}

	/**
	 * @param organismId the organismId to set
	 */
	public void setOrganismId(int organismId) {
		this.organismId = organismId;
	}

	/**
	 * @return the uniquename
	 */
	public String getUniquename() {
		return uniquename;
	}

	/**
	 * @param uniquename the uniquename to set
	 */
	public void setUniquename(String uniquename) {
		this.uniquename = uniquename;
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	@Override
	public String toString() {
		return "geneLinks ["
				+ "\n"+"id=" + id + ", "
				+ "\n"+"tagId" + tagId + ", "
				+ "\n"+"uniquename=" + uniquename + ", "
				+ "\n"+"name=" + name + ", "
				+ "\n"+"organismId=" + organismId + ", "
				+ "\n"+"]";
	}
	

}
