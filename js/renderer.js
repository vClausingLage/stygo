const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.SphereGeometry( 15, 32, 16 );
const material = new THREE.MeshBasicMaterial( { color: 0xfeeff } );
const sphere = new THREE.Mesh( geometry, material );
scene.add( sphere );

// Entfernung
camera.position.z = 50;

// Render-Funktion
function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();